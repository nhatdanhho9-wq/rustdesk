/// The windows targets in the publish time order.
enum WindowsTarget {
  naw, // not a windows target
  xp,
  vista,
  w7,
  w8,
  w8_1,
  w10,
  w11
}

/// A convenient method to transform a build number to the corresponding windows version.
extension WindowsTargetExt on int {
  WindowsTarget get windowsVersion => getWindowsTarget(this);
}
