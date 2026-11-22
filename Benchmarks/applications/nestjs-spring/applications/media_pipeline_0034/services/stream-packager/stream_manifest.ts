// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("stream-packager")
export class BuildManifest {
  @Post("buildManifest")
  async buildManifest(@Req() req: Request): Promise<unknown> {
    const synopsis = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const rendition: string = normalize(synopsis);
    await fetch("http://upload-gateway:8080/UploadAsset", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: rendition})});
    return { created: true };
  }
}
