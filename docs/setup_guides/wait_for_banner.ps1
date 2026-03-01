param (
    [string]$SourceFolder = "C:\Users\Alex Rosales\Desktop\Zapatos",
    [string]$DestinationFolder = "C:\Users\Alex Rosales\.gemini\antigravity\scratch\Zapatosproject\brand",
    [string]$BannerNamePattern = "*banner*"
)

Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "   VORA ELITE - AUTOMATIZACION DE BANNER PROMOCIONAL   " -ForegroundColor Cyan
Write-Host "=======================================================" -ForegroundColor Cyan
Write-Host "Monitorizando la carpeta $SourceFolder en busqueda del banner de Gemini..."

$found = $false

while (-not $found) {
    # Busca cualquier imagen que contenga "banner" en su nombre
    $files = Get-ChildItem -Path $SourceFolder -Filter $BannerNamePattern -File -Include *.jpg,*.png,*.webp -ErrorAction SilentlyContinue

    if ($files.Count -gt 0) {
        $found = $true
        foreach ($file in $files) {
            Write-Host "¡Banner detectado! -> $($file.Name)" -ForegroundColor Green
            $DestPath = Join-Path -Path $DestinationFolder -ChildPath $file.Name
            
            # Copiar a la carpeta de brand del repositorio
            Copy-Item -Path $file.FullName -Destination $DestPath -Force
            Write-Host "Banner copiado exitosamente a /brand." -ForegroundColor Yellow
            
            # TODO: Aquí se puede anidar el comando API para subir la foto a Google Business y FB.
        }
    } else {
        Start-Sleep -Seconds 10
    }
}

Write-Host "Operación de banner finalizada." -ForegroundColor Cyan
