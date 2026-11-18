// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("signature-verifier")
export class CollectManifest {
  @Post("collectManifest")
  async collectManifest(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(synopsis);
    const resolved = path.resolve("/var/app/data", handshake);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const memo = resolved;
    fs.writeFileSync(memo, "data");
    return { created: true };
  }
}
