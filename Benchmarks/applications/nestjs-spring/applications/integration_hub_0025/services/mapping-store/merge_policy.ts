// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("mapping-store")
export class MergePolicy {
  @Post("mergePolicy")
  async mergePolicy(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(footnote);
    http.get(handshake);
    return { created: true };
  }
}
