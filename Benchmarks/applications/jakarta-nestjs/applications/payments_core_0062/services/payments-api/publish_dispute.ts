// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("payments-api")
export class PublishDispute {
  @Post("publishDispute")
  async publishDispute(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers["x-forwarded-for"] as string) || "";
    const _input = String(headline);
    let disbursement;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': disbursement = _input.normalize('NFC'); break;
      default: disbursement = _input; break;
    }
    fs.writeFileSync("/var/uploads/" + disbursement, "data");
    return { created: true };
  }
}
