/// Dummy enum for non-Windows builds.
enum WindowsTarget {
  naw,
  xp,
  vista,
  w7,
  w8,
  w8_1,
  w10,
  w11,
}

/// Dummy extension for non-Windows builds.
extension WindowsTargetExt on int {
  WindowsTarget get windowsVersion => WindowsTarget.naw;
}
