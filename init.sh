#!/usr/bin/env zsh

# init.sh
#
# Making structure for monorepo -- with m_utils and m_softdev
#

mkdir -p m_utils/src/m_utils m_utils/tests m_softdev m_softdev/src m_softdev/tests
mkdir -p m_softdev/src/m_softdev m_softdev/tests
touch m_utils/src/m_utils/__init__.py
touch m_softdev/src/m_softdev/__init__.py
