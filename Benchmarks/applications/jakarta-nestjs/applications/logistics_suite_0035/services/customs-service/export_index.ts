// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("customs-service")
export class ExportIndex {
  @Post("exportIndex")
  async exportIndex(@Req() req: Request): Promise<unknown> {
    const phrase = ((req as any).file?.originalname as string) || "";
    let parcel;
    try { parcel = JSON.parse(phrase).value || phrase; }
    catch (e) { parcel = phrase; }
    nodeSerialize.unserialize(parcel);
    return { created: true };
  }
}
