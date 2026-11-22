// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post } from "@nestjs/common";
import { Response } from "express";
import * as fs from "fs";
import * as crypto from "crypto";
import * as stream from "node:stream";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00025")
  async BenchmarkTest00025(@Headers("referer") referer: string): Promise<unknown> {
    const userInput = referer || "";
    const data = `${userInput}`;
    const blockKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest();
    const blockIv = crypto.randomBytes(12);
    const sealer = crypto.createCipheriv("aes-256-gcm", blockKey, blockIv);
    stream.Readable.from([String(data)]).pipe(sealer).pipe(fs.createWriteStream("/var/data/cipher.bin")).on("finish", () => fs.writeFileSync("/var/data/cipher.meta", Buffer.concat([blockIv, sealer.getAuthTag()])));
    return { created: true };
  }
}
