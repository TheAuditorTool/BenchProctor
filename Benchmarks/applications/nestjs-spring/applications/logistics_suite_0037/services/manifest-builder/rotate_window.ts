// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("manifest-builder")
export class RotateWindow {
  @Post("rotateWindow")
  async rotateWindow(@Req() req: Request): Promise<unknown> {
    const footnote = (req.cookies?.session_token as string) || "";
    let consignment;
    try { consignment = JSON.parse(footnote).value || footnote; }
    catch (e) { consignment = footnote; }
    net.connect(80, new URL(String(consignment)).hostname);
    return { created: true };
  }
}
