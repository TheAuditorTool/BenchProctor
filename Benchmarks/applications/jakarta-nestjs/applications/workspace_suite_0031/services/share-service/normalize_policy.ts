// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("share-service")
export class NormalizePolicy {
  @Post("normalizePolicy")
  async normalizePolicy(@Req() req: Request): Promise<unknown> {
    const caption = (req.body as string) || "";
    const formData = Object.freeze({ payload: caption });
    const synopsis = formData.payload;
    nodeSerialize.unserialize(synopsis);
    return { created: true };
  }
}
