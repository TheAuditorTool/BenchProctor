// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("document-api")
export class AuditBatch {
  @Post("auditBatch")
  async auditBatch(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.referer as string) || "";
    const payload = { get value() { return wording; } };
    const addendum = payload.value;
    const fileContent = fs.readFileSync("/var/app/data/" + addendum, "utf8");
    return fileContent;
  }
}
