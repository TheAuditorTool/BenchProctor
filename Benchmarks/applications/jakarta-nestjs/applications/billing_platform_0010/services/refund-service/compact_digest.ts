// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("refund-service")
export class CompactDigest {
  @Post("compactDigest")
  async compactDigest(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers["x-forwarded-for"] as string) || "";
    const _input = String(headline);
    let remittance;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': remittance = _input.normalize('NFC'); break;
      default: remittance = _input; break;
    }
    const resolved = path.resolve("/var/app/data", remittance);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const dunning = resolved;
    fs.unlinkSync(dunning);
    return { created: true };
  }
}
