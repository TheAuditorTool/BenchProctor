// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("manifest-builder")
export class AuditReport {
  @Post("auditReport")
  async auditReport(@Req() req: Request): Promise<unknown> {
    const citation = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return citation; } };
    const parcel = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(parcel))) { throw new BadRequestException({error:"invalid"}); }
    const consignment = parcel;
    const fileContent = fs.readFileSync("/var/app/data/" + consignment, "utf8");
    return fileContent;
  }
}
