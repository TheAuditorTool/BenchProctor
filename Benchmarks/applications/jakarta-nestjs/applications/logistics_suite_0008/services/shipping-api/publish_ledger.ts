// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("shipping-api")
export class PublishLedger {
  @Post("publishLedger")
  async publishLedger(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.host as string) || "";
    const _input = String(caption);
    let consignment;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': consignment = _input.normalize('NFC'); break;
      default: consignment = _input; break;
    }
    http.get(consignment);
    return { created: true };
  }
}
