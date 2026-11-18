// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("payments-api")
export class AuditSnapshot {
  @Post("auditSnapshot")
  async auditSnapshot(@Req() req: Request): Promise<unknown> {
    const caption = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return caption; } };
    const ledger = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(ledger))) { throw new BadRequestException({error:"invalid"}); }
    const remittance = ledger;
    const fileContent = fs.readFileSync("/var/app/data/" + remittance, "utf8");
    return fileContent;
  }
}
