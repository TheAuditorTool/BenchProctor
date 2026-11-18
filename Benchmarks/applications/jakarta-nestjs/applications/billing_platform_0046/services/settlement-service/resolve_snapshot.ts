// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("settlement-service")
export class ResolveSnapshot {
  @Post("resolveSnapshot")
  async resolveSnapshot(@Req() req: Request): Promise<unknown> {
    const remark = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const _raw = remark;
    const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
    net.connect(80, new URL(String(remittance)).hostname);
    return { created: true };
  }
}
