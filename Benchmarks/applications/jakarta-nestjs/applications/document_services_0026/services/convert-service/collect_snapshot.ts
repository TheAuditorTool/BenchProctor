// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("convert-service")
export class CollectSnapshot {
  @Post("collectSnapshot")
  async collectSnapshot(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["x-forwarded-for"] as string) || "";
    const _input = String(preface);
    let addendum;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': addendum = _input.normalize('NFC'); break;
      default: addendum = _input; break;
    }
    const resolved = path.resolve("/var/app/data", addendum);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const dossier = resolved;
    fs.unlinkSync(dossier);
    return { created: true };
  }
}
