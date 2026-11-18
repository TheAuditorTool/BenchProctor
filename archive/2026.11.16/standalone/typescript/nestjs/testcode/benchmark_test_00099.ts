// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, UploadedFile, UseInterceptors, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as fs from "fs";
import { FileInterceptor } from "@nestjs/platform-express";
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
  @Post("BenchmarkTest00099")
  @UseInterceptors(FileInterceptor("file"))
  async BenchmarkTest00099(@UploadedFile() file: Express.Multer.File): Promise<unknown> {
    const userInput = file?.originalname || "";
    const _raw = userInput;
    const data = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(data)) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    fs.writeFileSync("/var/uploads/" + processed, "data");
    return { created: true };
  }
}
