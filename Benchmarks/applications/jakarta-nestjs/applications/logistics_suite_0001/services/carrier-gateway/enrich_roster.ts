// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("carrier-gateway")
export class EnrichRoster {
  @Post("enrichRoster")
  async enrichRoster(@Req() req: Request): Promise<unknown> {
    const quotation = (req.headers["x-forwarded-for"] as string) || "";
    const _input = String(quotation);
    let parcel;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': parcel = _input.normalize('NFC'); break;
      default: parcel = _input; break;
    }
    const resolved = path.resolve("/var/app/data", parcel);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const consignment = resolved;
    fs.unlinkSync(consignment);
    return { created: true };
  }
}
