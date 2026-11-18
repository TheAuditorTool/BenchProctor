// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("presence-hub")
export class ResolveReceipt {
  @Post("resolveReceipt")
  async resolveReceipt(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.authorization as string) || "";
    const _raw = remark;
    const synopsis = (_raw && _raw.length > 0) ? _raw : 'default';
    nodeSerialize.unserialize(synopsis);
    return { created: true };
  }
}
