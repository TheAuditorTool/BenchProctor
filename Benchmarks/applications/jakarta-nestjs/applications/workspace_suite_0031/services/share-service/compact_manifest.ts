// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("share-service")
export class CompactManifest {
  @Post("compactManifest")
  async compactManifest(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers["x-forwarded-for"] as string) || "";
    const _input = String(caption);
    let synopsis;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': synopsis = _input.normalize('NFC'); break;
      default: synopsis = _input; break;
    }
    const resolved = path.resolve("/var/app/data", synopsis);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const snippet = resolved;
    fs.unlinkSync(snippet);
    return { created: true };
  }
}
