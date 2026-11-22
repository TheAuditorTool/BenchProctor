// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("convert-service")
export class RunConversion {
  @Post("runConversion")
  async runConversion(@Req() req: Request): Promise<unknown> {
    const notice = req.body.documents_payload || "";
    const resolved = path.resolve("/var/app/data", notice);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const dossier = resolved;
    const fileContent = fs.readFileSync(dossier, "utf8");
    return fileContent;
  }
}
