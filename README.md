<p align="center">
  <img src="ssvm.png" width="128" align="center"/>
</p>
<p align="center">
  <b>Siri Shortcuts Virtual Machine (SSVM)</b>
</p>

**SSVM** is a compiler infrastructure for **Siri Shortcuts programming languages**. It consists of both an intermediate representation (**SSVM IR**) and the backend that compiles this IR to a runnable Siri Shortcut. It is inspired by the LLVM project.

### Motivation
Previously, there had been many attempts to create compilers to programmatically generate Siri Shortcuts. Many of them were abonded because Shortcuts change with every IOS/iPadOS/macOS update, and it is really hard to keep track. Languages that are currently maintained try to keep up with the updates themselves. However, this problem can be solved by creating a common compiler backend, which will be the only component that requires change with IOS/iPadOS/macOS updates.

### Intermediate Representation: SSVM IR

With every update, Apple adds new **action**s, and modify existing ones. **SSVM IR** is resilient to the upcoming updates, and compatible with different Shortcuts versions. For each target version, the **backend** is capable of compiling given SSVM IR representation to a runnable Shortcut.

Siri Shortcuts programming language developers can write a frontend that compile their own language to SSVM IR, thus easily keep their language up-to-date! 

<p align="center">
  <img src="diagram-light.png#gh-light-mode-only" width="720" align="center"/>
  <img src="diagram-dark.png#gh-dark-mode-only" width="720" align="center"/>
</p>
