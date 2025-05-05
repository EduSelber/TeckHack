import asyncio
from sslyze import Scanner, ServerScanRequest
from sslyze.server_setting import ServerNetworkLocation


async def run_scan():
    hostname = input("Digite a URL ou IP (ex: testssl.sh): ").strip()

    try:
        server = ServerNetworkLocation(hostname=hostname, port=443)

        scanner = Scanner()
        scanner.queue_scan(
            ServerScanRequest(
                server_location=server,
                scan_commands={"certificate_info", "heartbleed"}
            )
        )

        # Aguarda e coleta os resultados
        async for scan_result in scanner.get_results():
            print("\n🔐 Informações do certificado:")

            cert_info = scan_result.scan_result.certificate_info
            subject = getattr(cert_info.certificate_deep_analysis, "subject", "N/A")
            issuer = getattr(cert_info.certificate_deep_analysis, "issuer", "N/A")
            validade = getattr(cert_info.certificate_deep_analysis, "not_valid_after", "N/A")

            print(f"  - Assunto: {subject}")
            print(f"  - Emitido por: {issuer}")
            print(f"  - Validade até: {validade}")

            print("\n❤️ Verificação Heartbleed:")
            heartbleed = scan_result.scan_result.heartbleed
            vulnerable = getattr(heartbleed, "is_vulnerable_to_heartbleed", "Desconhecido")
            print(f"  - Vulnerável? {vulnerable}")

    except Exception as e:
        print(f"\n❌ Erro ao escanear {hostname}: {e}")


if __name__ == "__main__":
    asyncio.run(run_scan())
