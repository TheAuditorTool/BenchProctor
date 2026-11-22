// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("carrier-gateway")
export class FetchProfile {
  @Post("fetchProfile")
  async fetchProfile(@Req() req: Request): Promise<unknown> {
    const quotation = (req.headers["x-forwarded-for"] as string) || "";
    const _input = String(quotation);
    let parcel;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': parcel = _input.normalize('NFC'); break;
      default: parcel = _input; break;
    }
    fs.writeFileSync("/var/uploads/" + parcel, "data");
    return { created: true };
  }
}
