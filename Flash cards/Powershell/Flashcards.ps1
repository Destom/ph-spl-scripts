$exit = ""
$category = Get-ChildItem ..\FlashCards

Write-Host -BackgroundColor Black -ForegroundColor Green "Welcome to Flashcards we currently have`n $category`n`nWhich Catergory do you want to study"

$choice = read-host

$cards = Import-csv ..\FlashCards\$choice.csv

while ($exit -ne "y")
{
    $card = Get-Random $cards.name
    cls
    Write-Host $card

    Read-Host

    cls

    $cards | Where-Object name -Like $card
    $exit = Read-Host "do you want to exit (Y/N)"
}
