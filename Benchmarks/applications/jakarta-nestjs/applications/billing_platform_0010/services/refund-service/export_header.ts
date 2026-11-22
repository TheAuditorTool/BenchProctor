// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("refund-service")
export class ExportHeader {
  @Post("exportHeader")
  async exportHeader(@Req() req: Request): Promise<unknown> {
    const headline = (req.body as string) || "";
    const payload = { get value() { return headline; } };
    const remittance = payload.value;
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(remittance)) { throw new ForbiddenException({error:"forbidden"}); }
    const dunning = "/var/app/data/" + remittance;
    fs.writeFileSync(dunning, "data");
    return { created: true };
  }
}
