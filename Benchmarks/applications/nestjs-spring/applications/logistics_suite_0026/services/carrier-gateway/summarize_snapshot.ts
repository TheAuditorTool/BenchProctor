// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("carrier-gateway")
export class SummarizeSnapshot {
  @Post("summarizeSnapshot")
  async summarizeSnapshot(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.origin as string) || "";
    const _input = String(citation);
    let parcel;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': parcel = _input.normalize('NFC'); break;
      default: parcel = _input; break;
    }
    http.get(parcel);
    return { created: true };
  }
}
