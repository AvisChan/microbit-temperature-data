input.onButtonPressed(Button.A, function () {
    let Temperature = 0
    microIoT.microIoT_http_post(
    "Temperature:" + Temperature,
    "",
    "",
    10000
    )
})
microIoT.microIoT_initDisplay()
microIoT.microIoT_WIFI("618_3", "Avis@001")
