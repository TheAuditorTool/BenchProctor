// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("log-shipper")
export class ResolveWindow {
  @Post("resolveWindow")
  async resolveWindow(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.origin as string) || "";
    const _input = String(caption);
    let gauge;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': gauge = _input.normalize('NFC'); break;
      default: gauge = _input; break;
    }
    http.get(gauge);
    return { created: true };
  }
}
