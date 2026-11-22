// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("share-service")
export class LoadReceipt {
  @Post("loadReceipt")
  async loadReceipt(@Req() req: Request): Promise<unknown> {
    const caption = (req.cookies?.session_token as string) || "";
    const _raw = caption;
    const synopsis = (_raw && _raw.length > 0) ? _raw : 'default';
    const resolved = path.resolve("/var/app/data", synopsis);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const snippet = resolved;
    const fileContent = fs.readFileSync(snippet, "utf8");
    return fileContent;
  }
}
