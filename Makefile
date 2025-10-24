# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 Lincoln Wallace

SYSTEMS = $(subst -plus-,+,$(sort $(shell spread -list :tests/smoke/uname | cut -d : -f 2)))

.PHONY:
$(foreach s,$(SYSTEMS),spread-$s): spread-%:
	$(strip spread -artifacts artifacts garden:$(subst +,-plus-,$*):)

.PHONY:
check: $(foreach s,$(SYSTEMS),spread-$s)
