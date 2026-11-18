// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("archive-store")
export class MergeConversion {
  @Post("mergeConversion")
  async mergeConversion(@Req() req: Request): Promise<unknown> {
    const note = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const addendum: string = normalize(note);
    const resolved = path.resolve("/var/app/data", addendum);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const dossier = resolved;
    fs.writeFileSync(dossier, "data");
    return { created: true };
  }
}
