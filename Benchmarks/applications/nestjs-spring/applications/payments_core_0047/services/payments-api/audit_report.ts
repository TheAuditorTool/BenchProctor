// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("payments-api")
export class AuditReport {
  @Post("auditReport")
  async auditReport(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body?.field as string) || "";
    const _input = String(footnote);
    let remittance;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': remittance = _input.normalize('NFC'); break;
      default: remittance = _input; break;
    }
    fs.writeFileSync("/var/uploads/" + remittance, "data");
    return { created: true };
  }
}
