# Maintainer: nobody <nobody@example.com>
pkgname=midistar
pkgver=0.0.1
pkgrel=1
pkgdesc="Connects USB MIDI devices"
url="https://example.com"
license=(BSD)
depends=(python alsa-utils systemd)
arch=(any)

package(){
install -Dm755 "${srcdir}"/midistar.py "${pkgdir}"/usr/share/midistar/midistar.py
install -Dm644 "${srcdir}"/midistar.service "${pkgdir}"/usr/lib/systemd/system/midistar.service
install -Dm644 "${srcdir}"/99-midistar.rules "${pkgdir}"/etc/udev/rules.d/99-midistar.rules
}
