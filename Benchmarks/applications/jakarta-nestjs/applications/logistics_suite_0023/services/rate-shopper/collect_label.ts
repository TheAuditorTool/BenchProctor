// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("rate-shopper")
export class CollectLabel {
  @Post("collectLabel")
  async collectLabel(@Req() req: Request): Promise<unknown> {
    const caption = ((req as any).file?.originalname as string) || "";
    let parcel;
    try { parcel = JSON.parse(caption).value || caption; }
    catch (e) { parcel = caption; }
    nodeSerialize.unserialize(parcel);
    return { created: true };
  }
}
