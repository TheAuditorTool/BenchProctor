// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("address-validator")
export class ValidateReport {
  @Post("validateReport")
  async validateReport(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["x-forwarded-for"] as string) || "";
    const _input = String(summary);
    let consignment;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': consignment = _input.normalize('NFC'); break;
      default: consignment = _input; break;
    }
    const resolved = path.resolve("/var/app/data", consignment);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const parcel = resolved;
    fs.unlinkSync(parcel);
    return { created: true };
  }
}
