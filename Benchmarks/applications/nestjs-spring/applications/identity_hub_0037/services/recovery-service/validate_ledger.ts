// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("recovery-service")
export class ValidateLedger {
  @Post("validateLedger")
  async validateLedger(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(remark);
    const persona: string = readInput();
    return shared.escapeHtml(persona);
  }
}
