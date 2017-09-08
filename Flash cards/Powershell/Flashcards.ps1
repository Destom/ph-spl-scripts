$exit = ""
$category = Get-ChildItem ..\FlashCards

Write-Host -BackgroundColor Black -ForegroundColor Green "Welcome to Flashcards we currently have`n $category`n`nWhich Catergory do you want to study"

$choice = read-host

$cards = Import-csv ..\FlashCards\$choice.csv

while ($exit -ne "y")
{
    $card = Get-Random $cards
    cls
    Write-Host $card.name

    Read-Host

    cls

    $card.name
    $card.description
    $exit = Read-Host "do you want to exit (Y/N)"
}
