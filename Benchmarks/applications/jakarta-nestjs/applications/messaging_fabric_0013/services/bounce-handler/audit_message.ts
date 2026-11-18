// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("bounce-handler")
export class AuditMessage {
  @Post("auditMessage")
  async auditMessage(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.field as string) || "";
    const _input = String(summary);
    let bulletin;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': bulletin = _input.normalize('NFC'); break;
      default: bulletin = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { throw new BadRequestException({error:"invalid"}); }
    const snippet = bulletin;
    const fileContent = fs.readFileSync("/var/app/data/" + snippet, "utf8");
    return fileContent;
  }
}
