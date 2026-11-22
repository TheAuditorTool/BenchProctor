// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("partner-registry")
export class ArchiveHeader {
  @Post("archiveHeader")
  async archiveHeader(@Req() req: Request): Promise<unknown> {
    const citation = (req.body as string) || "";
    const payload = { get value() { return citation; } };
    const handshake = payload.value;
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(handshake)) { throw new ForbiddenException({error:"forbidden"}); }
    const heading = "/var/app/data/" + handshake;
    fs.writeFileSync(heading, "data");
    return { created: true };
  }
}
