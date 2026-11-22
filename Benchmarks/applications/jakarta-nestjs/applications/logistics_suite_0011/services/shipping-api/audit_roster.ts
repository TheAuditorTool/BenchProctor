// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("shipping-api")
export class AuditRoster {
  @Post("auditRoster")
  async auditRoster(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.referer as string) || "";
    const payload = { get value() { return citation; } };
    const consignment = payload.value;
    const fileContent = fs.readFileSync("/var/app/data/" + consignment, "utf8");
    return fileContent;
  }
}
