// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("signature-verifier")
export class AuditPartner {
  @Post("auditPartner")
  async auditPartner(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(heading);
    const handshake: string = readInput();
    return shared.escapeHtml(handshake);
  }
}
