// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post } from "@nestjs/common";
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
  @Post("BenchmarkTest00080")
  async BenchmarkTest00080(@Body("multipart_field") mf: string): Promise<unknown> {
    const userInput = mf || "";
    const data = String(userInput).split(/[ \t]+/).join(" ");
    const blockKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest();
    stream.Readable.from([String(data)]).pipe(crypto.createCipheriv("aes-256-ecb", blockKey, null)).pipe(fs.createWriteStream("/var/data/cipher.bin"));
    return { created: true };
  }
}
