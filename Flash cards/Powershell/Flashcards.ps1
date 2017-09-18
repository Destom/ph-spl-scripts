$exit = ""
$category = Get-ChildItem ..\FlashCards

Write-Host -BackgroundColor Black -ForegroundColor Green "Welcome to Flashcards we currently have`n $category`n`nWhich Catergory do you want to study"

$choice = read-host

$cards = Import-csv ..\FlashCards\$choice.csv

while ($exit -ne "y")
{
    $card = Get-Random $cards
    cls
    Write-Host -BackgroundColor Black -ForegroundColor Green $card.name

    Read-Host

    cls

    Write-Host -BackgroundColor Black -ForegroundColor Green $card.name
    Write-Host -BackgroundColor Black -ForegroundColor Green $card.description
    $exit = Read-Host "do you want to exit (Y/N)"
}
