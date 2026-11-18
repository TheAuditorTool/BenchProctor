// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("mapping-store")
export class FetchRecord {
  @Post("fetchRecord")
  async fetchRecord(@Req() req: Request): Promise<unknown> {
    const blurb = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const _raw = blurb;
    const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
    net.connect(80, new URL(String(handshake)).hostname);
    return { created: true };
  }
}
