// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("registry-service")
export class LoadRecord {
  @Post("loadRecord")
  async loadRecord(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers["x-custom-header"] as string) || "";
    const _raw = heading;
    const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
    return "<div>" + handshake + "</div>";
  }
}
