// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("supplier-feed")
export class VerifyDigest {
  @Post("verifyDigest")
  async verifyDigest(@Req() req: Request): Promise<unknown> {
    const memo = (req.body as string) || "";
    const payload = { get value() { return memo; } };
    const backorder = payload.value;
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(backorder)) { throw new ForbiddenException({error:"forbidden"}); }
    const restock = "/var/app/data/" + backorder;
    fs.writeFileSync(restock, "data");
    return { created: true };
  }
}
