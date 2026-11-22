// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("redaction-service")
export class ApplyRedaction {
  @Post("applyRedaction")
  async applyRedaction(@Req() req: Request): Promise<unknown> {
    const synopsis = req.body.documents_payload || "";
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(synopsis)) { throw new ForbiddenException({error:"forbidden"}); }
    const addendum = "/var/app/data/" + synopsis;
    fs.writeFileSync(addendum, "data");
    return { created: true };
  }
}
