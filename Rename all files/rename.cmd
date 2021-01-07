$path = "$"
$filter = "*.jpg"

get-childitem -path $path -filter $filter |
rename-item -newname {$_.name -replace "filenames", "newfilenames"}