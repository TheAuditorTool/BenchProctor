// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Res, UploadedFile, UseInterceptors } from "@nestjs/common";
import { Response } from "express";
import * as nodeUtil from "util";
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
  @Post("BenchmarkTest00508")
  @UseInterceptors(FileInterceptor("file"))
  async BenchmarkTest00508(@UploadedFile() file: Express.Multer.File, @Res({ passthrough: true }) res: Response): Promise<unknown> {
    const userInput = file?.originalname || "";
    const data = nodeUtil.format("%s", userInput);
    res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
    return { created: true };
  }
}
