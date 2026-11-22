// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("consent-registry")
export class ValidateLedger {
  @Post("validateLedger")
  async validateLedger(@Req() req: Request): Promise<unknown> {
    const remark = (req.body as string) || "";
    const payload = { get value() { return remark; } };
    const persona = payload.value;
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(persona)) { throw new ForbiddenException({error:"forbidden"}); }
    const notice = "/var/app/data/" + persona;
    fs.writeFileSync(notice, "data");
    return { created: true };
  }
}
