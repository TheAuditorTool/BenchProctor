// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Res, UploadedFile, UseInterceptors } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00283")
  @UseInterceptors(FileInterceptor("file"))
  async BenchmarkTest00283(@UploadedFile() file: Express.Multer.File, @Res({ passthrough: true }) res: Response): Promise<unknown> {
    const userInput = file?.originalname || "";
    const data = `${userInput}`;
    res.setHeader("Set-Cookie", "session=" + encodeURIComponent(String(data)) + "; Path=/; HttpOnly; SameSite=Strict");
    return { created: true };
  }
}
